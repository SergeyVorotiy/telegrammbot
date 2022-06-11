import requests
from config import API_TOKEN, VALUES


class InvalidArgumentsException(Exception):
    pass


class InvalidArgumentsCountException(Exception):
    pass


class Price:
    @staticmethod
    def get_price(message):
        result = ''
        try:
            message_lengh = len(message)
            if message_lengh == 3:
                quote, base, amount = message
                quote = str(quote).title()
                base = str(base).title()
                f_amount = float(amount)
                if quote not in VALUES.keys():
                    raise InvalidArgumentsException(f'аргумент {quote} указан неверно')
                if base not in VALUES.keys():
                    raise InvalidArgumentsException(f'Аргумент {base} указан неверно')
                url = f"https://api.apilayer.com/fixer/convert?to={VALUES[base]}&from={VALUES[quote]}&amount={amount}"
                response = requests.get(url, API_TOKEN)
                result = f"цена {amount} {quote} в {base} - {json.loads(response.content)['result']} "
            elif message_lengh < 3:
                raise InvalidArgumentsCountException('Аргументов недостаточно')
            else:
                raise InvalidArgumentsCountException('Слишком много аргументов')
        except InvalidArgumentsCountException as e:
            return f'Ошибка: {e}'
        except InvalidArgumentsException as e:
            return f'Ошибка: {e}'
        except ValueError as e:
            return f'Ошибка: третий аргумент должен быть числом'
        except Exception as e:
            return f'Ошибра на стороне бота: {e}'
        else:
            return result