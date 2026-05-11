class LinearRegression:
    
    def __init__(self, learning_rate, max_iter):
        
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        
    def predict(self,X):
        
        prediction = X @ self.weights + self.bias
        
        return prediction
    
    def fit(self, X, y):
        
        n_samples,n_features = X.shape
        
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for i in range(self.max_iter):
            prediction = self.predict(X)
            loss = self.loss(y, prediction)
            dw, db = self.calculate_gradients(X, y, prediction)
            self.weights -= self.learning_rate * dw 
            self.bias -= self.learning_rate * db
            
        return 
    
    def loss(self, y, prediction):
        
        error = y - prediction
        mse = np.mean(np.square(error))
        
        return mse
    
    def calculate_gradients(self, X, y, prediction):
        
        n_samples = X.shape[0]
        
        error = prediction - y
        
        dw = (1 / n_samples) * (np.transpose(X) @ error)
        db = np.mean(error)
        
        return dw, db
    

