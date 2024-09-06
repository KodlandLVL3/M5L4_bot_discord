import os
import discord
from discord.ext import commands
from logic import process_image
from config import TOKEN

# Инициализация бота
intents = discord.Intents.default()
intents.message_content = True  # Необходимо для получения содержимого сообщений
bot = commands.Bot(command_prefix="!", intents=intents)

# Событие при готовности бота
@bot.event
async def on_ready():
    print(f'Мы вошли как {bot.user}')

# Команда старт
@bot.command(name='start')
async def start(ctx):
    await ctx.send("Привет! Отправьте мне фото, и я замаскирую лица на нем.")

# Обработчик изображений
@bot.event
async def on_message(message):
    # Проверяем, что сообщение не от самого бота
    if message.author == bot.user:
        return
    
    # Проверяем, что сообщение содержит вложение
    if message.attachments:
        try:
            attachment = message.attachments[0]
            # Проверяем, что это изображение
            if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Определяем расширение файла
                file_ext = '.jpg' if attachment.filename.lower().endswith('.jpg') else '.png'
                
                # Задаем пути для входного и выходного файла
                input_file_path = f"input{file_ext}"
                output_file_path = f"output{file_ext}"
                
                # Сохраняем входное изображение
                await attachment.save(input_file_path)

                # Обрабатываем изображение (размытие лиц)
                process_image(input_file_path, output_file_path)

                # Отправляем обработанное изображение
                await message.channel.send(file=discord.File(output_file_path))

                # Удаляем временные файлы
                os.remove(input_file_path)
                os.remove(output_file_path)
            else:
                await message.channel.send("Пожалуйста, отправьте изображение в формате PNG, JPG или JPEG.")
        
        except Exception as e:
            await message.channel.send(f"Произошла ошибка: {str(e)}")
    
    # Не забываем обрабатывать команды
    await bot.process_commands(message)

@bot.command(name='info')
async def help_command(ctx):
    await ctx.send("Отправьте мне фото, и я размою лица на нем.")

if __name__ == "__main__":
    bot.run(TOKEN)