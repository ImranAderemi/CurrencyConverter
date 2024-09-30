import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/98000db504d479e3486f12a4/latest/{base_currency}" #After testing and consulting my peers, I was advised to change the url to use the base_currency that the user inputs, as opposed to defaulting to USD as the base currency
    response = requests.get(url)
    data = response.json()
    
    #Checking if the api is connected successfully
    if response.status_code == 200:
        return data["conversion_rates"].get(target_currency, None)
    
    else:
        print("Sorry, there was an error:)", data.get("error-type"))
        return None


#performs the currency conversion by multpilying the amount by the exchange rate of the currency
def convert_currency(amount, exchange_rate):
    return amount * exchange_rate



def main():
    api_key = '98000db504d479e3486f12a4'
    
    print("Hello, Welcome to my Currency Converter :)")

    #For the sake of clarity to the user, I added the list of available currencies and their common names
    print("Please look below for your desired 3-Letter identier in the list of available currencies")
    print("\n")

    print("AED - United Arab Emirates dirham")
    print("AFN - Afghan Afghani")
    print("ALL - Albanian Lek")
    print("AMD - Armenian Dram")
    print("ANG - Netherlands Antillean Guilder")
    print("AOA - Angolan Kwanza")
    print("ARS - Argentine Peso")
    print("AUD - Australian Dollar")
    print("AWG - Aruban Florin")
    print("AZN - Azerbaijani Manat")
    print("BAM - Bosnia-Herzegovina Convertible Mark")
    print("BBD - Barbadian Dollar")
    print("BDT - Bangladeshi Taka")
    print("BGN - Bulgarian Lev")
    print("BHD - Bahraini Dinar")
    print("BIF - Burundian Franc")
    print("BMD - Bermudian Dollar")
    print("BND - Brunei Dollar")
    print("BOB - Bolivian Boliviano")
    print("BRL - Brazilian Real")
    print("BSD - Bahamian Dollar")
    print("BTN - Bhutanese Ngultrum")
    print("BWP - Botswana Pula")
    print("BYN - Belarusian Ruble")
    print("BZD - Belize Dollar")
    print("CAD - Canadian Dollar")
    print("CDF - Congolese Franc")
    print("CHF - Swiss Franc")
    print("CLP - Chilean Peso")
    print("CNY - Chinese Yuan")
    print("COP - Colombian Peso")
    print("CRC - Costa Rican Colón")
    print("CUP - Cuban Peso")
    print("CVE - Cape Verdean Escudo")
    print("CZK - Czech Koruna")
    print("DJF - Djiboutian Franc")
    print("DKK - Danish Krone")
    print("DOP - Dominican Peso")
    print("DZD - Algerian Dinar")
    print("EGP - Egyptian Pound")
    print("ERN - Eritrean Nakfa")
    print("ETB - Ethiopian Birr")
    print("EUR - Euro")
    print("FJD - Fijian Dollar")
    print("FKP - Falkland Islands Pound")
    print("FOK - Faroese Króna")
    print("GBP - British Pound Sterling")
    print("GEL - Georgian Lari")
    print("GGP - Guernsey Pound")
    print("GHS - Ghanaian Cedi")
    print("GIP - Gibraltar Pound")
    print("GMD - Gambian Dalasi")
    print("GNF - Guinean Franc")
    print("GTQ - Guatemalan Quetzal")
    print("GYD - Guyanese Dollar")
    print("HKD - Hong Kong Dollar")
    print("HNL - Honduran Lempira")
    print("HRK - Croatian Kuna")
    print("HTG - Haitian Gourde")
    print("HUF - Hungarian Forint")
    print("IDR - Indonesian Rupiah")
    print("ILS - Israeli New Shekel")
    print("IMP - Isle of Man Pound")
    print("INR - Indian Rupee")
    print("IQD - Iraqi Dinar")
    print("IRR - Iranian Rial")
    print("ISK - Icelandic Króna")
    print("JEP - Jersey Pound")
    print("JMD - Jamaican Dollar")
    print("JOD - Jordanian Dinar")
    print("JPY - Japanese Yen")
    print("KES - Kenyan Shilling")
    print("KGS - Kyrgyzstani Som")
    print("KHR - Cambodian Riel")
    print("KID - Kiribati Dollar")
    print("KMF - Comorian Franc")
    print("KRW - South Korean Won")
    print("KWD - Kuwaiti Dinar")
    print("KYD - Cayman Islands Dollar")
    print("KZT - Kazakhstani Tenge")
    print("LAK - Lao Kip")
    print("LBP - Lebanese Pound")
    print("LKR - Sri Lankan Rupee")
    print("LRD - Liberian Dollar")
    print("LSL - Lesotho Loti")
    print("LYD - Libyan Dinar")
    print("MAD - Moroccan Dirham")
    print("MDL - Moldovan Leu")
    print("MGA - Malagasy Ariary")
    print("MKD - Macedonian Denar")
    print("MMK - Myanmar Kyat")
    print("MNT - Mongolian Tögrög")
    print("MOP - Macanese Pataca")
    print("MRU - Mauritanian Ouguiya")
    print("MUR - Mauritian Rupee")
    print("MVR - Maldivian Rufiyaa")
    print("MWK - Malawian Kwacha")
    print("MXN - Mexican Peso")
    print("MYR - Malaysian Ringgit")
    print("MZN - Mozambican Metical")
    print("NAD - Namibian Dollar")
    print("NGN - Nigerian Naira")
    print("NIO - Nicaraguan Córdoba")
    print("NOK - Norwegian Krone")
    print("NPR - Nepalese Rupee")
    print("NZD - New Zealand Dollar")
    print("OMR - Omani Rial")
    print("PAB - Panamanian Balboa")
    print("PEN - Peruvian Sol")
    print("PGK - Papua New Guinean Kina")
    print("PHP - Philippine Peso")
    print("PKR - Pakistani Rupee")
    print("PLN - Polish Złoty")
    print("PYG - Paraguayan Guaraní")
    print("QAR - Qatari Riyal")
    print("RON - Romanian Leu")
    print("RSD - Serbian Dinar")
    print("RUB - Russian Ruble")
    print("RWF - Rwandan Franc")
    print("SAR - Saudi Riyal")
    print("SBD - Solomon Islands Dollar")
    print("SCR - Seychellois Rupee")
    print("SDG - Sudanese Pound")
    print("SEK - Swedish Krona")
    print("SGD - Singapore Dollar")
    print("SHP - Saint Helena Pound")
    print("SLE - Sierra Leonean Leone")
    print("SLL - Sierra Leonean Leone")
    print("SOS - Somali Shilling")
    print("SRD - Surinamese Dollar")
    print("SSP - South Sudanese Pound")
    print("STN - São Tomé and Príncipe Dobra")
    print("SYP - Syrian Pound")
    print("SZL - Swazi Lilangeni")
    print("THB - Thai Baht")
    print("TJS - Tajikistani Somoni")
    print("TMT - Turkmenistani Manat")
    print("TND - Tunisian Dinar")
    print("TOP - Tongan Paʻanga")
    print("TRY - Turkish Lira")
    print("TTD - Trinidad and Tobago Dollar")
    print("TVD - Tuvaluan Dollar")
    print("TWD - New Taiwan Dollar")
    print("TZS - Tanzanian Shilling")
    print("UAH - Ukrainian Hryvnia")
    print("UGX - Ugandan Shilling")
    print("USD - United States Dollar")
    print("UYU - Uruguayan Peso")
    print("UZS - Uzbekistani Som")
    print("VES - Venezuelan Bolívar")
    print("VND - Vietnamese Dong")
    print("VUV - Vanuatu Vatu")
    print("WST - Samoan Tala")
    print("XAF - Central African CFA Franc")
    print("XCD - East Caribbean Dollar")
    print("XDR - Special Drawing Rights")
    print("XOF - West African CFA Franc")
    print("XPF - CFP Franc")
    print("YER - Yemeni Rial")
    print("ZAR - South African Rand")
    print("ZMW - Zambian Kwacha")
    print("ZWL - Zimbabwean Dollar")




    while True: #I chose to use a while loop so that the user can repeat and perform multiple conversions

        print("\n")
        base_currency = input("What currency would you like to convert from? (e.g., USD, EUR, GBP): ").upper()
        #base_currency - The currency that the user wishes the conversion to be based on (the currency that they want to convert)

        target_currency = input("What currency would you like to convert into? (e.g., USD, EUR, GBP): ").upper()
        #target_currency - The currency that the user whishes to convert into
        
        amount = float(input(f"Please enter the amount you would like to convert in {base_currency}: "))
        #amount - The amount that they wish to convert

        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)


        #checks if the exchange rate is valid
        if exchange_rate is not None:

            converted_amount = convert_currency(amount, exchange_rate)
            print("\n")
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
            print(f"1 {base_currency} = {exchange_rate} {target_currency}")
            
        else:
            print("\n")
            print(f"Sorry, I couldn't get the exchange rate for {base_currency} to {target_currency}. It's possible that you entered the wrong 3-letter currency identifier, Please check that this is not the case.")
        
        # Ask if the user wants to perform another conversion
        print("\n")
        again = input("Would you like to perform another conversion? (yes/no): ").lower() #Note to self - Don't forget to add '.lower' after testing
        if again != "yes":

            print("\n")
            print("Thank you for using my currency converter, Goodbye")
            break

        else:
            main()

if __name__ == "__main__":
    main()
