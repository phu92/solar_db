#-*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import load_model
from tensorflow import keras
from keras.preprocessing import image
import time
pd.options.display.float_format = '{:.2f}'.format
# https://ibb.co/sqzfGhf
st.image('solar-park-g59755c796_1280.jpg')
st.write('')
st.write('')
#========================태양광 불러오기==============================
region = ['지역을 선택해주세요','전국','서울','광주','부산','대전','대구','인천','울산',
'전남','전북','경남','경북','강원도','경기도','제주','세종','충남','충북']

choice = st.selectbox('태양광 발전량을 알고싶은 지역을 선택해주세요. (첫 로딩시 30초 정도 소요 됩니다.)', region)
if choice is not None:
    st.write('본 정보는 한국전력거래소에 등록된 설비용량 기준입니다. ')

solar_power = 0
def solar_cal(sol_cal):
    solar_power = float(sol_cal.iloc[23][1])
    if st.button('탄소배출량 계산!'):
        st.write('========================================================')
        st.write(f'해당 지역의 오늘 태양광 누적 발전 예상량은 {solar_power}KWh 입니다.')
        st.write(f'한국 전력의 전력 생산 1KWh당 탄소발생량으로 환산하면{np.round(solar_power*0.424,2)}Kg 입니다')
        st.write(f'30년생 소나무 {int((solar_power*0.424)/6.6)} 그루가 1년 동안 흡수해야하는 양입니다.')
        st.write(f'태양광 발전으로 오늘 하루 탄소발생량 약 {np.round(np.round(solar_power*0.424,2) - np.round(solar_power*0.424/8.33,2),2)}Kg을 절감했습니다.')
        st.write('========================================================')
    return sol_cal
    
if choice == '전국':
    my_df = pd.read_csv('my_df.csv', header=None, float_precision='round_trip')
    my_df = my_df.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    my_df = my_df.drop(index=0)
    my_df2 = pd.read_csv('my_df.csv')
    csv_conv = my_df2.to_csv().encode('utf-8-sig')
    all_solar = my_df2.iloc[23][1]

    if st.button('시각 데이터 확인'):
        chart_df = my_df.iloc[:,1]
        chart_df = chart_df.reset_index(drop = True)
        chart_df = chart_df.astype(float)
        st.area_chart(chart_df,width=720)

        chart_df2 = my_df.iloc[:,2]
        chart_df2 = chart_df2.reset_index(drop = True)
        chart_df2 = chart_df2.astype(float)
        st.line_chart(chart_df2,width=720)
    if st.button('탄소배출량 계산!'):
        st.write('========================================================')
        st.write(f'오늘 전국의 태양광 누적 발전 예상량은 {all_solar}KWh 입니다.')
        st.write(f'한국 전력의 전력 생산 1KWh당 탄소발생량으로 환산하면{np.round(all_solar*0.424,2)}Kg 입니다')
        st.write(f'30년생 소나무 {int((all_solar*0.424)/6.6)} 그루가 1년 동안 흡수해야하는 양입니다.')
        st.write(f'태양광 발전으로 오늘 하루 탄소발생량 약 {np.round(np.round(all_solar*0.424,2) - np.round(all_solar*0.424/8.33,2),2)}Kg을 절감했습니다.')
        st.write('========================================================')
    st.dataframe(my_df)

    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '제주':
    제주 = pd.read_csv('제주.csv', header=None, float_precision='round_trip')
    csv_conv = 제주.to_csv().encode('utf-8-sig')
    제주 = 제주.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    제주 = 제주.drop(index=0)
    solar_cal(제주)
    st.dataframe(제주)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '경기도':
    경기 = pd.read_csv('경기.csv', header=None, float_precision='round_trip')
    csv_conv = 경기.to_csv().encode('utf-8-sig')
    경기 = 경기.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    경기 = 경기.drop(index=0)    
    solar_cal(경기)
    st.dataframe(경기)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '강원도':
    강원 = pd.read_csv('강원.csv', header=None, float_precision='round_trip')
    csv_conv = 강원.to_csv().encode('utf-8-sig')
    강원 = 강원.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    강원 = 강원.drop(index=0)
    solar_cal(강원)
    st.dataframe(강원)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '경북':
    경북 = pd.read_csv('경북.csv', header=None, float_precision='round_trip')
    csv_conv = 경북.to_csv().encode('utf-8-sig')
    경북 = 경북.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    경북 = 경북.drop(index=0)    
    solar_cal(경북)
    st.dataframe(경북)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '경남':
    경남 = pd.read_csv('경남.csv', header=None, float_precision='round_trip')
    csv_conv = 경남.to_csv().encode('utf-8-sig')
    경나 = 경남.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    경남 = 경남.drop(index=0)
    solar_cal(경남)
    st.dataframe(경남)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '전북':
    전북 = pd.read_csv('전북.csv', header=None, float_precision='round_trip')
    csv_conv = 전북.to_csv().encode('utf-8-sig')
    전북 = 전북.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    전북 = 전북.drop(index=0)
    solar_cal(전북)
    st.dataframe(전북)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '전남':
    전남 = pd.read_csv('전남.csv', header=None, float_precision='round_trip')
    csv_conv = 전남.to_csv().encode('utf-8-sig')
    전남 = 전남.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    전남 = 전남.drop(index=0)
    solar_cal(전남)
    st.dataframe(전남)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '울산':
    울산 = pd.read_csv('울산.csv', header=None, float_precision='round_trip')
    csv_conv = 울산.to_csv().encode('utf-8-sig')
    울산 = 울산.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    울산 = 울산.drop(index=0)
    solar_cal(울산)
    st.dataframe(울산)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '인천':
    인천 = pd.read_csv('인천.csv', header=None, float_precision='round_trip')
    csv_conv = 인천.to_csv().encode('utf-8-sig')
    인천 = 인천.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    인천 = 인천.drop(index=0)
    solar_cal(인천)
    st.dataframe(인천)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '대구':
    대구 = pd.read_csv('대구.csv', header=None, float_precision='round_trip')
    csv_conv = 대구.to_csv().encode('utf-8-sig')
    대구 = 대구.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    대구 = 대구.drop(index=0)
    solar_cal(대구)
    st.dataframe(대구)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '대전':
    대전 = pd.read_csv('대전.csv', header=None, float_precision='round_trip')
    csv_conv = 대전.to_csv().encode('utf-8-sig')
    solar_cal(대전)
    대전 = 대전.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    대전 = 대전.drop(index=0)
    st.dataframe(대전)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '부산':
    부산 = pd.read_csv('부산.csv', header=None, float_precision='round_trip')
    csv_conv = 부산.to_csv().encode('utf-8-sig')
    solar_cal(부산)
    부산 = 부산.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    부산 = 부산.drop(index=0)
    st.dataframe(부산)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '광주':
    광주 = pd.read_csv('광주.csv', header=None, float_precision='round_trip')
    csv_conv = 광주.to_csv().encode('utf-8-sig')
    광주 = 광주.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    광주 = 광주.drop(index=0)
    solar_cal(광주)
    st.dataframe(광주)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '서울':
    서울 = pd.read_csv('서울.csv', header=None, float_precision='round_trip')
    csv_conv = 서울.to_csv().encode('utf-8-sig')
    서울 = 서울.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    서울 = 서울.drop(index=0)
    solar_cal(서울)
    st.dataframe(서울)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '세종':
    세종 = pd.read_csv('세종.csv', header=None, float_precision='round_trip')
    csv_conv = 세종.to_csv().encode('utf-8-sig')
    세종 = 세종.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    세종 = 세종.drop(index=0)
    solar_cal(세종)
    st.dataframe(세종)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '충남':
    충남 = pd.read_csv('충남.csv', header=None, float_precision='round_trip')
    csv_conv = 충남.to_csv().encode('utf-8-sig')
    충남 = 충남.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    충남 = 충남.drop(index=0)
    solar_cal(충남)
    st.dataframe(충남)
    st.download_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv')
if choice == '충북':
    st.write('충청북도는 발전 설비가 없어 출력되지 않습니다.')
    # 충북 = pd.read_csv('충북.csv', header=None, float_precision='round_trip')
    # csv_conv = 충북.to_csv().encode('utf-8-sig')
    # st.dataframe(충북)
    # solar_cal(충북)
    # 충북 = 충북.rename(columns={0:'발전량(KW)', 1:'누적발전량(KWh)', 2:'일사량(W/㎡)', 3:'기온(℃)'})
    # 충북 = 충북.drop(index=0)
    #if  st.nload_button('표 데이터를 저장할 수 있습니다.',data=csv_conv,mime='text/csv'):
       
#=========================이미지 인식 부====================================
st.write('')
st.write('')
st.write('')

Image = st.file_uploader('하늘 사진을 올려주세요 (현재 스트림릿의 문제로 이미지 업로드만 됩니다.)',type=['jpg','jpeg','png'])

if Image is not None:
    st.write(Image)
    # files = os.listdir('/app/testhack')
    # st.write(files)
    # st.image(Image, width=180)
    # my_model = load_model('my_model.h5')
    # img_data = image.load_img('example4.jpg', target_size=(180,180))
    # img_data

    # img_data = tf.expand_dims(img_data, 0)

    # predictions = my_model.predict(img_data)
    # score = tf.nn.softmax(predictions[0])
    # filenames = ['맑은 날', '흐린 날', '일몰 혹은 일출']
    # st.write(
    #     "해당 사진의 날씨는 {} 입니다."
    #     .format(filenames[np.argmax(score)])
    # )

st.write('')
st.write('')
st.write('')
model_ex = st.selectbox('모델 예시 입니다.',('예제를 선택해 주세요.','example1.jpg','example2.jpg','example3.jpg','example4.jpg','사용한 코드'))
if model_ex == '예제를 선택해 주세요.':
    st.write('')
elif model_ex == '사용한 코드':
    st.code('''    my_model = load_model('my_model.h5')
    img_data = image.load_img('이미지 경로', target_size=(180,180))
    img_data

    img_data = tf.expand_dims(img_data, 0)

    predictions = my_model.predict(img_data)
    score = tf.nn.softmax(predictions[0])
    filenames = ['맑은 날', '흐린 날', '일몰 혹은 일출']
    st.write(
        "해당 사진의 날씨는 {} 입니다."
        .format(filenames[np.argmax(score)])
    ) ''')
else:
    my_model = load_model('my_model.h5')
    img_data = image.load_img(model_ex, target_size=(180,180))
    img_data

    img_data = tf.expand_dims(img_data, 0)

    predictions = my_model.predict(img_data)
    score = tf.nn.softmax(predictions[0])
    filenames = ['맑은 날', '흐린 날', '일몰 혹은 일출']
    st.write(
        "해당 사진의 날씨는 {} 입니다."
        .format(filenames[np.argmax(score)])
    )
    st.image(model_ex)
#===========================테스트 부분==================================
list_1 = ['선택지를 골라주세요!', '바다','산','집','해외여행','캠핑']
list_2 = ['선택지를 골라주세요!','클래식','가요','POP','힙합','재즈']
list_3 = ['선택지를 골라주세요!','봄','여름','가을','겨울','다 좋아!']
list_4 = ['선택지를 골라주세요!','독서','음악감상','운동','드라이브','게임']
list_5 = ['선택지를 골라주세요!','은하수를 여행하는 히치하이커','아이로봇','매트릭스','아이언맨','월-E']
st.sidebar.header('나와 어울리는 신재생 에너지는?')
st.sidebar.image('outline_battery_unknown_black_48dp.png')
selected_item_1 = st.sidebar.selectbox("코로나가 끝나 놀러 가고 싶은 당신은?", list_1)
selected_item_2 = st.sidebar.selectbox("당신의 음악 취향은?",list_2)
selected_item_3 = st.sidebar.selectbox("좋아하는 계절은?",list_3)
selected_item_4 = st.sidebar.selectbox("평소에 즐겨하는 취미는?", list_4)
selected_item_5 = st.sidebar.selectbox("가장 좋아하는 인공지능 영화는?", list_5)

geo_count = 0
water_count = 0
wind_count = 0
solar_count = 0
H2_count = 0

if selected_item_1 == '바다':
    water_count +=1
elif selected_item_1 == '산':
    wind_count +=1
elif selected_item_1 == '집':
    H2_count +=1
elif selected_item_1 == '해외여행':
    geo_count +=1
elif selected_item_1 == '캠핑':
    solar_count +=1

if selected_item_2 == '클래식':
    wind_count +=1
elif selected_item_2 == '가요':
    solar_count +=1
elif selected_item_2 == 'POP':
    geo_count +=1
elif selected_item_2 == '힙합':
    H2_count +=1
elif selected_item_2 == '재즈':
    water_count +=1

if selected_item_3 == '봄':
    solar_count +=1
elif selected_item_3 == '여름':
    water_count +=1
elif selected_item_3 == '가을':
    wind_count +=1
elif selected_item_3 == '겨울':
    geo_count +=1
elif selected_item_3 == '다 좋아':
    H2_count +=1

if selected_item_4 == '독서':
    wind_count +=1
elif selected_item_4 == '음악감상':
    geo_count +=1
elif selected_item_4 == '운동':
    water_count +=1
elif selected_item_4 == '드라이브':
    H2_count +=1
elif selected_item_4 == '게임':
    solar_count +=1

if selected_item_5 == '은하수를 여행하는 히치하이커':
    geo_count +=1
elif selected_item_5 == '아이로봇':
    wind_count +=1
elif selected_item_5 == '매트릭스':
    water_count +=1
elif selected_item_5 == '아이언맨':
    H2_count +=1
elif selected_item_5 == '월-E':
    solar_count +=1

result = {'지열 발전':geo_count,'풍력 발전':wind_count,'수력 발전':water_count,
        '수소 발전':H2_count,'태양광 발전':solar_count}
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

if selected_item_1 != '선택지를 골라주세요!' and st.sidebar.button('결과 출력!'):
    st.sidebar.write(f'당신과 어울리는 신재생 에너지는')
    st.sidebar.write(f'☆☆☆　{sorted_result[0][0]}입니다!　☆☆☆')
    st.sidebar.write('↓ 아래에서 신재생 에너지를 확인해보세요')

st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')

if st.sidebar.button('수력'):
    st.sidebar.image('수력 발전.jpg')
if st.sidebar.button('지열'):
    st.sidebar.image('지열 발전.jpg')
if st.sidebar.button('태양광'):
    st.sidebar.image('태양광 발전.jpg')
if st.sidebar.button('풍력'):
    st.sidebar.image('풍력 발전.jpg')
if st.sidebar.button('수소'):
    st.sidebar.image('수소에너지.jpg')