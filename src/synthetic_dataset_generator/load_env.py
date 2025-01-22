import os
from pathlib import Path
from typing import Dict

def load_env_file(env_path: Path | str) -> Dict[str, str]:
    """
    Load environment variables from a .env file.
    
    Args:
        env_path: Path to the .env file
        
    Returns:
        Dict of environment variables loaded
    
    Raises:
        FileNotFoundError: If the .env file doesn't exist
    """
    env_vars = {}
    
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                os.environ[key] = value
                env_vars[key] = value
                
    return env_vars


def init_environment() -> Dict[str, str]:
    """
    Initialize environment variables from .env file in project root.
    
    Returns:
        Dict of environment variables loaded
        
    Raises:
        FileNotFoundError: If the .env file doesn't exist
    """
    root_dir = Path(__file__).parent.parent.parent
    env_file = root_dir / ".env"
    
    if not env_file.exists():
        raise FileNotFoundError(
            f"Environment file not found at {env_file}. "
            "Please create a .env file in the project root directory."
        )
        
    return load_env_file(env_file) 