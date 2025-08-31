from sklearn.preprocessing import StandardScaler

def preprocess_data(df, features):
    if not features:
        raise ValueError("Tidak ada fitur yang dipilih untuk clustering!")
    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler
