# shceduled
Позволяет импортировать расписание студента t-университета в google календарь 
Перед использование нужно получить идентификатор календаря google:
![изображение](https://github.com/Limoos21/shceduled/assets/89832541/538b80f1-52dc-4842-949f-340c80a90888)
![Снимок экрана 2023-06-17 04311](https://github.com/Limoos21/shceduled/assets/89832541/b6dd4c9c-a0c9-41df-8eb2-b770d1edab81)
Записываем этот идентификатор в код:
![изображение](https://github.com/Limoos21/shceduled/assets/89832541/8c73000d-af96-44cf-9a93-e04ef6f61b29)
Теперь необходимо предоставить разрешения на добавление событий в твой календарь, добавьте эту строку nikita@shcedulenikita.iam.gserviceaccount.com
![изображение](https://github.com/Limoos21/shceduled/assets/89832541/4ebb136a-4974-4271-bd39-ddd3dac774f3)
НЕ ЗАБУДЬТЕ В КОДЕ ВВЕСТИ СВОЙ ЛОГИН И ПАРОЛЬ ОТ edu.donstu
Дополнительно, если не хочешь постоянно запускать код для обновения расписания, можешь добавить его в автозагрузку, для этого измени файл run.bat, в эту переменную set script_path запиши путь до основного скрипта :
![изображение](https://github.com/Limoos21/shceduled/assets/89832541/e0501918-94e2-4a3b-9356-f5861ea286b7)
затем в файлt run.vbs отредактируй эту строчку: "WshShell.Run chr(34) & "C:\Users\Nikita\Documents\GitHub\shceduled\run.bat" & Chr(34), 0" и запиши в нее путь до run.bat
![изображение](https://github.com/Limoos21/shceduled/assets/89832541/84c0f7ce-b91c-416b-9df4-8481cf45ac2f)
последним действием тебе нужно создай ярлык файла run.vbs и поместить его в папку C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
для того, чтобы скрипт автоматически запускался :)


