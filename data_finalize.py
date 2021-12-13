import pandas as pd

main = pd.read_csv('./main_info.csv')
spec = pd.read_csv('./spec_info.csv')

main['lowest_price'] = main['lowest_price'].str.replace(',','').astype(float)
main['montly_sales'] = main['montly_sales'].str.replace(' sold/month','').str.replace('.','').str.replace('k','00').fillna(0).astype(int)
main['original_price'] = main.original_price.str.replace('RM','').str.replace(',','').astype(float)
main['original_price'] = main['original_price'].fillna(0)
main['discount_rate'] = main.discount_rate.str.replace('%','').fillna(0).astype(int)
main = main.drop(columns=['Unnamed: 0','link']).fillna(0)



spec.rename(columns={'ratings(amount)':'ratings'},inplace=True)
spec['ratings'] = spec['ratings'].str.replace('k','000').str.replace('.','').fillna(0).astype(int)
spec.loc[(spec.ratings > 10000), 'ratings'] = spec.ratings / 10

spec['total_sales'] = spec['total_sales'].str.replace('k','000').str.replace('.','').fillna(0).astype(int)
spec.loc[(spec.total_sales > 10000), 'total_sales'] = spec.total_sales / 10
spec.loc[(spec.total_sales > 100000), 'total_sales'] = spec.total_sales / 100

spec['favorites'] = spec['favorites'].str.replace('Favorite ','').str.replace('(','').str.replace(')','').str.replace('.','').str.replace('k','00').fillna(0).astype(int)

spec['weight'] = spec['weight'].str.replace('g','').str.replace('.','').str.replace('k','000').fillna(0).astype(int)
spec.loc[(spec.weight > 10000) & (spec.weight < 99999), 'weight'] = spec.weight / 10
spec.loc[(spec.weight > 100000), 'weight'] = spec.weight / 100

spec['warranty'] = spec['warranty'].str.split(' ').str[0].fillna(0).replace('No','0').astype(int)

spec['capacity'] = spec['capacity'].str.replace('L','').astype(float).fillna(0)

spec['stock'] = spec['stock'].fillna(0).astype(int)

spec['power'] = spec['power'].str.replace('W','').fillna(0).astype(int)

spec['brand'] = spec['brand'].fillna(0).replace(0,'Others')

spec.drop(columns='Unnamed: 0',inplace=True)



spec = spec.fillna(0)


final = pd.concat([main,spec], axis = 1)

# final.to_csv('./product_info_list.csv', sep=',',na_rep='NaN', encoding='utf_8_sig')

# from sqlalchemy import create_engine
# engine = create_engine('postgresql://xdzwpuop:uW8dSE7OdUye6fuCni7x4Gy5atztstog@arjuna.db.elephantsql.com:5432/xdzwpuop')

# # check=engine.has_table('shopee_product')
# # print(check) #boolean
# # if check == False:
# final.to_sql("shopee_product", engine, if_exists='replace',index=False)
# # final.to_sql("shopee_product", engine)

final.drop(columns=['Unnamed: 0','product_title'],inplace=True)
final['period'] = final['total_sales'] / final['montly_sales']
final['period'] = final['period'].round(2)

import numpy as np
final['marketability'] = round((np.sqrt((final['favorites'] + final['ratings']) * final['star'] * final['total_sales'])) / final['period']).fillna(0)

#brand 제외
df = final[['lowest_price','discount_rate','weight','warranty','capacity','stock','power','marketability']]

df.to_csv('./info_for_model.csv', sep=',',na_rep='NaN', encoding='utf_8_sig')