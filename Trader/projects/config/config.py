ALPHA_VANTAGE_API_KEY = 'Z9YEXKMHS2FYS0DS'
TELEGRAM_API_KEY = '1869926849:AAGS7AVD-b4XbUpSF3BW7yc2SruE8sDHOFg'

__developer_mode = True

__bot_name = 'Golden Cross X'
__telegrm_interval = 2

if not __developer_mode:
    telegram_hour = __telegrm_interval * 3600
else:
    telegram_hour = 30

ticker = 'ATOM'
time_frames = {'1': '1min', '5': '5min', '15': '15min',
               '30': '30min', '60': '60min'}  # bars
selected_tf = '1min'

order_percentage = 0.95

notify_when_there_is_no_signal = True


# telegram bot mesajlari
start_message = (f"Merhaba, {__bot_name} botuna hoş geldiniz. Bu bot ile belirlediğiniz mum preiyotları ile {ticker} üzerinden  GOLDENCROSS tespit edebilirsiniz."
                 f"{__bot_name} botu size her {__telegrm_interval} saatte bir tespit ettiği Golden cross sinyallerini gönderecektir."
                 "\nBaşlamadan önce bazı ayarlamalar yapmak bu bot üzerinden alacağınız verimi arttıracaktır. "
                 "Bunlar: \n \n /setbar x : [1, 3, 5, 15, 30, 60] yazarak botun kullancağı bar büyüklerini ayarlayabilirsiniz. Örneğin "
                 '\n "/setbar 3" yazarak 3\'er dakikalık mumlar kullabilirsiniz. \n \n '
                 f'/setcash x : yazarak sanal paranız ile tespit edilen sinyaller ile kısmi "PaperTrading" yapabilirsiniz. Böylelikler kar-zarar hesaplaması yapabilirsiniz. Örneğin: \n'
                 "/setcash 10000 yazarak işlemlerinizi 10000 dolarınız varmış gibi değerlendirebilirsiniz. \n \n"
                 "/cash yazarak güncel paranızı görebilirsiniz. \n \n"
                 f"Bot otomatik olarak paranın {order_percentage * 100}% ini tespit ettiği sinyallerde uygular. Bu oranı isterseniz \n"
                 "/setorderpercentage x : Z[0 < x <= 100] yazarak paranızın yüzde kaçı ile işlem yapılacağını ayarlayabilirsiniz. \n \n"
                 "/help yazarak tüm komutlara ulaşbilirsiniz. \n \n"
                 "/info yazarak profil bilgilerinize ulaşbilirsiniz. \n \n"
                 "Dilerserniz /stop yazarak bu botu durdurabilirsiniz."
                 )

help_message = ("/info: Güncel profil bilgileri \n"
                "/help: Komut listesi \n"
                "/setbar x: dakikalık bar periyodu. [1, 3, 5, 15, 30, 60] \n"
                "/setcash x: para ekleme \n"
                "/cash güncel bakiye \n"
                "/setorderpercentage işlem yüzdesi \n"
                "/stop botu durdur \n"
                )

stop_message = "Bot durduruldu."
off_message = "Bot zaten kapalı."

get_bar_message = "Bar periyodu: "
bar_message = "Bar periyodu değiştirildi."
bar_error_message = "Lütfen geçerli aralıkta bir komut verin. \n Örneğin: \"/setbar 30\" gibi"

get_cash_message = "Güncel bakiye: "
cash_message = "Bakiye güncellendi."
cash_error_message = "Sadece pozitif bir sayı girebilirsiniz. \n Örneğin: \"/setcash 30000\" gibi"
no_cash_message = "Kaydınız bulunmamaktadır."

get_per_message = "İşlem yüzdesi: "
per_message = "İşlem yüzdesi güncellendi."
per_error_message = "Lütfen 1 ile 100 arasında bir tam sayı giriniz."

get_ticker_message = "Ticker: "
general_error = "Bot üzerinde teknik bir aksaklık oluştu. Daha sonra tekrar deneyiniz."

non = 'Sinyal tespit edilemedi'
