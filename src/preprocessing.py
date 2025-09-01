import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, features):
    X = df[features].copy()

    for col in X.columns:
        if X[col].dtype == "object":
            X[col] = (
                X[col]
                .astype(str)
                .str.replace(",", "", regex=False)  
                .str.replace(" ", "", regex=False)  
            )
        X[col] = pd.to_numeric(X[col], errors="coerce")

    X = X.dropna()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler, X.index  
