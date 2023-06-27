with open("names.txt", 'r', encoding='utf-8') as file_with_names:
    with open("template.txt", 'r', encoding='utf-8') as body_of_the_mail:
        body = body_of_the_mail.read()

        for name in file_with_names:
            mail = 'Dear ' + name.strip() + '\n' + body

            with open(name.strip() + '.txt', 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)