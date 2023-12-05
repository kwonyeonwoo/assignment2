import pandas as pd

def top_player(dataset_df,years):
  selected = dataset_df[dataset_df['year']==years]
  top_h = selected.sort_values(by=['H'], ascending=False )[:10]['batter_name']
  top_avg = selected.sort_values(by=['avg'], ascending=False)[:10]['batter_name']
  top_hr = selected.sort_values(by=['HR'], ascending=False)[:10]['batter_name']
  top_obp = selected.sort_values(by=['OBP'], ascending=False)[:10]['batter_name']
  return top_h, top_avg, top_hr, top_obp

def print_players(best_h,best_avg,best_hr,best_obp,years):
  print("Top 10 players in hits(안타) for", years,":", best_h.values)
  print("Top 10 players in average(타율) for",years,":", best_avg.values)
  print("Top 10 players in homerun(홈런) for",years,":" ,best_hr.values)
  print("Top 10 players in OBP(출루율) for", years,":" ,best_obp.values,"\n")

def highest_war(dataset_df):
  players_2018 = dataset_df[dataset_df['year']==2018].sort_values(by=['war'],ascending=False)
  best_c = players_2018[players_2018['cp']=="포수"][:1]['batter_name']
  best_1b = players_2018[players_2018['cp']=="1루수"][:1]['batter_name']
  best_2b = players_2018[players_2018['cp']=="2루수"][:1]['batter_name']
  best_3b = players_2018[players_2018['cp']=="3루수"][:1]['batter_name']
  best_ss = players_2018[players_2018['cp']=="유격수"][:1]['batter_name']
  best_lf = players_2018[players_2018['cp']=="좌익수"][:1]['batter_name']
  best_cf = players_2018[players_2018['cp']=="중견수"][:1]['batter_name']
  best_rf = players_2018[players_2018['cp']=="우익수"][:1]['batter_name']
  return best_c , best_1b, best_2b, best_3b, best_ss, best_lf, best_cf, best_rf

def find_corr(dataset_df):
  all_data = dataset_df[['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']]
  result = all_data.corrwith(all_data.salary)
  highest = result.drop('salary').idxmax()
  return highest

if __name__=='__main__':
  datas = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
  data_df = pd.DataFrame(datas)

  season = [2015,2016,2017,2018]

  for i in season:
    top_h, top_avg, top_hr, top_obp = top_player(data_df,i)
    print_players(top_h,top_avg,top_hr,top_obp,i)

  best_c, best_1b, best_2b, best_3b, best_ss, best_lf, best_cf, best_rf = highest_war(data_df)

  print("highest war c  player(포수)   in 2018 :", best_c.values)
  print("highest war 1b player(1루수)  in 2018 :", best_1b.values)
  print("highest war 2b player(2루수)  in 2018 :", best_2b.values)
  print("highest war 3b player(3루수)  in 2018 :", best_3b.values)
  print("highest war ss player(유격수) in 2018 :", best_ss.values)
  print("highest war lf player(좌익수) in 2018 :", best_lf.values)
  print("highest war cf player(중견수) in 2018 :", best_cf.values)
  print("highest war rf player(우익수) in 2018 :", best_rf.values)

  result = find_corr(data_df)
  print("\nhighest correlation with salary :",result)
