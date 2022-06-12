import pickle
import streamlit as st 
import numpy as np



model=pickle.load(open('marketing_price.sav','rb'))




def prediction_data(budget):
    input=np.array([budget])
    input_reshape=input.reshape(-1,1)
    predicton=model.predict(input_reshape)
    print(predicton)
    return predicton




def main():
    st.title(" To Find the sales using buget ")

    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">To find the sales using budgets data ML App </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    budget=st.slider("Enter your amount",10,200,10)


    if st.button("Predict"):
        output=prediction_data(budget)
        st.success('The sales is {}'.format(output[0],3))
if __name__=='__main__':
    main()