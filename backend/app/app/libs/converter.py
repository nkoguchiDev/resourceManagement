class ModelConverter:
    def __init__(self):
        pass

    @staticmethod
    def to_cypher_object(model) -> str:
        model_dict = model.dict(exclude_none=True)
        key_values = [
            f'{key}: "{model_dict.get(key)}"'
            for key in list(model_dict.keys())
        ]
        return f'{{{",".join(key_values)}}}'

    @staticmethod
    def byte_key_value_to_dict(data: dict) -> dict:
        return {key.decode(): val.decode()
                for key, val in data.items()}
