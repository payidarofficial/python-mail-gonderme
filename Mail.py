# Pâyidar
from smtplib import SMTP

try:
    payidar_1 = 'Test'
    payidar_2 = 'Selam Arda! Nasılsın Bugün.'
    genel = "Subcjet: {0}\n\n{1}".format(payidar_1,payidar_2)

    # E Posta
    kendi_mail_adresim = "Emailiniz"
    sifrem = "Emailinizin Şifreniz"

    # Kime Gönderilecek
    gonderilecek = "Gönderilecek Kişinin Emaili"

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(kendi_mail_adresim,sifrem)
    mail.sendmail(kendi_mail_adresim,gonderilecek,genel.encode("utf-8"))
    print('Mail Gönderme Başarılı.')

except Exception as e:
    print('Hata Oluştu\n {0}'.format(e))
