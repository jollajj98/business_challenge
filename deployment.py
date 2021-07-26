import streamlit as st
import pickle
import pandas
# prepare data and model
pickle_file = open("model.pkl", "rb")
regressor = pickle.load(pickle_file)
postcodes_df = pandas.read_csv("postcodes_20190613.csv")
province_stats = pandas.read_csv("provinc_stats.csv", index_col=0)
# store html strings
safe = """
        <h1 style = "color:#FF8888; text-align:center; font-size:24px">ON TRACK FOR CONTAINMENT</h1>
        <p style = "color:white; text-align:center; font-size:18px">Caution necessary, but no need for concern</h1>
        """
low = """
        <h1 style = "color:#FF8888; text-align:center; font-size:24px">COMMUNITY SPREAD</h1>
        <p style = "color:white; text-align:center; font-size:18px">Take extra care around people</h1>
        """
medium = """
        <h1 style = "color:#FF8888; text-align:center; font-size:24px">ACCELERATED SPREAD</h1>
        <p style = "color:white; text-align:center; font-size:18px">Stay home as much as possible</h1>
        """
high = """
        <h1 style = "color:#FF8888; text-align:center; font-size:24px">TIPPING POINT</h1>
        <p style = "color:white; text-align:center; font-size:18px">The situation is critical and requires rigorous measures to be followed</h1>
        """
input_text="""
    <h1 style = "color:white;font-size:16px"> Enter a postcode</h1>
    """
description = """
        <h1 style = "color:#FF8888; text-align:center; font-size:24px">TRAVEL SAFELY IN THE NETHERLANDS</h1>
        <p style = "color:white; text-align:center; font-size:18px">A data-driven roadmap to assessing COVID risk in every region</h1>
        """


def predict(stats):
    res = regressor.predict(stats)
    st.write("RISK LEVEL : " + str(res))
    if (res < 1):
        risk = safe
    elif (res < 1.6):
        risk = low
    elif (res < 2.6):
        risk = medium
    else:
        risk = high
    return risk


def main():
    # page setup
    st.image("logo-01.png")
    line_break = "<br>"
    st.markdown(line_break, unsafe_allow_html=True)
    st.markdown(line_break, unsafe_allow_html=True)
    st.markdown(description, unsafe_allow_html=True)
    st.markdown(line_break, unsafe_allow_html=True)
    st.markdown(input_text, unsafe_allow_html=True)
    postcode = st.text_input("")

    if st.button("Predict risk level"):
        # look up which province the postcode is in
        province = postcodes_df.loc[postcodes_df['postal_code'] == str.upper(postcode), ['province']]
        for x in province["province"]:
            province = x
        st.markdown(line_break, unsafe_allow_html=True)
        st.write("You're travelling to : " + province)
        # look up stats for the province
        stats = province_stats.loc[province_stats['province'] == province]
        stats = stats.drop(["province"], axis = 1)
        # assign risk level through trained model
        result = predict(stats)
        st.markdown(result, unsafe_allow_html=True)
if __name__ == "__main__":
    main()