from pydantic import BaseModel, model_validator
from typing import Tuple, Optional, Dict, Any
import sys
import os

class MazeConfig(BaseModel):
    config_file: str
    width: int
    height: int
    entry: Tuple[int, int]
    exit_: Tuple[int, int]
    perfect: bool = True
    output_file: str = "maze.txt"
    seed: Optional[int] = None

    @model_validator(mode='before')
    def initialize_from_file(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        config_file = values.get('config_file')
        if not config_file or not os.path.isfile(config_file):
            print(f"Error: Configuration file '{config_file}' not found")
            sys.exit(1)

        config: Dict[str, str] = {}
        try:
            with open(config_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if '=' not in line:
                        print(f"Warning: Ignoring malformed line: {line}")
                        continue
                    key, value = line.split('=', 1)
                    config[key.strip().upper()] = value.strip()
        except Exception as e:
            print(f"Unexpected error while reading '{config_file}': {e}")
            sys.exit(1)

        # WIDTH ===============================================================
        if 'WIDTH' not in config:
            print("Configuration error: WIDTH must be provided")
            sys.exit(1)
        if not config['WIDTH'].isdigit() or int(config['WIDTH']) <= 3:
            print("Configuration error: WIDTH must be integer > 3")
            sys.exit(1)
        values['width'] = int(config['WIDTH'])

        # HEIGHT ==============================================================
        if 'HEIGHT' not in config:
            print("Configuration error: HEIGHT must be provided")
            sys.exit(1)
        if not config['HEIGHT'].isdigit() or int(config['HEIGHT']) <= 3:
            print("Configuration error: HEIGHT must be integer > 3")
            sys.exit(1)
        values['height'] = int(config['HEIGHT'])

        width = values['width']
        height = values['height']

        # ENTRY ===============================================================
        if 'ENTRY' not in config:
            print("Configuration error: ENTRY must be provided")
            sys.exit(1)
        try:
            entry_parts = [int(x) for x in config['ENTRY'].split(',')]
            if len(entry_parts) != 2:
                raise ValueError
            entry_x, entry_y = entry_parts
            if not (0 <= entry_x < width) or not (0 <= entry_y < height):
                raise ValueError
        except ValueError:
            print("Configuration error: ENTRY must be 'x,y' within bounds")
            sys.exit(1)
        values['entry'] = (entry_x, entry_y)

        # EXIT ================================================================
        if 'EXIT' not in config:
            print("Configuration error: EXIT must be provided")
            sys.exit(1)
        try:
            exit_parts = [int(x) for x in config['EXIT'].split(',')]
            if len(exit_parts) != 2:
                raise ValueError
            exit_x, exit_y = exit_parts
            if not (0 <= exit_x < width) or not (0 <= exit_y < height):
                raise ValueError
        except ValueError:
            print("Configuration error: EXIT must be 'x,y' within bounds")
            sys.exit(1)
        values['exit_'] = (exit_x, exit_y)

        if values['entry'] == values['exit_']:
            print("Configuration error: ENTRY and EXIT must be different")
            sys.exit(1)

        # PERFECT =============================================================
        if 'PERFECT' not in config:
            print("Configuration error: PERFECT must be provided (true/false)")
            sys.exit(1)
        perfect_str = config['PERFECT'].lower()
        if perfect_str not in ['true', 'false']:
            print("Configuration error: PERFECT must be 'true' or 'false'")
            sys.exit(1)
        values['perfect'] = (perfect_str == 'true')

        # OUTPUT_FILE =========================================================
        if 'OUTPUT_FILE' not in config or not config['OUTPUT_FILE']:
            print("Configuration error: OUTPUT_FILE must be provided")
            sys.exit(1)
        values['output_file'] = config['OUTPUT_FILE']

        # SEED (optional) =====================================================
        if 'SEED' in config:
            if not config['SEED'].isdigit():
                print("Configuration error: SEED must be an integer")
                sys.exit(1)
            values['seed'] = int(config['SEED'])

        print(f"✓ Configuration loaded successfully from '{config_file}'")
        return values
