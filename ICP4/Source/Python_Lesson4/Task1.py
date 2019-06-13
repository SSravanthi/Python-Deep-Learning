import pandas as pd

train_df = pd.read_csv('train.csv')
#test_df = pd.read_csv('test.csv')
X_train= train_df.drop("Survived",axis=1)
Y_train= train_df["Survived"]
#X_test= test_df.drop("PassengerId",axis=1).copy()
#print(train_df[train_df.isnull().any(axis=1)])

train_df['Sex'] = train_df['Sex'].map( {'female': 1, 'male': 0} ).astype(int)


#print(train_df['Sex'])

#print(train_df['Survived'].value_counts(dropna='False'))
print(train_df['Survived'].corr(train_df['Sex']))