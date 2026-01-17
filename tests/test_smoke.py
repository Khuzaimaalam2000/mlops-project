import pytest
from pathlib import Path

class TestCoreImports:
    """Verify core packages are importable."""
    def test_numpy(self):
        import numpy
        assert numpy.__version__

    def test_pandas(self):
        import pandas
        assert pandas.__version__

    def test_sklearn(self):
        import sklearn
        assert sklearn.__version__

class TestBasicFunctionality:
    """Verify packages work beyond just importing."""
    def test_numpy_array_operations(self):
        import numpy as np
        arr = np.array([1, 2, 3])
        assert arr.sum() == 6

    def test_pandas_dataframe_creation(self):
        import pandas as pd
        df = pd.DataFrame({'x': [1, 2, 3]})
        assert len(df) == 3

class TestProjectStructure:
    """Verify project structure is correct."""
    def test_src_is_package(self):
        assert Path("src/__init__.py").exists()

    def test_requirements_exists(self):
        assert Path("requirements.txt").exists()