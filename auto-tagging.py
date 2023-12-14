import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split

# Load the pre-processed movie review dataset
data = pd.read_csv("IMDB Dataset.csv", sep=",")

# Number of words to consider as features
num_features = 2000

# Create a tokenizer
tokenizer = Tokenizer(num_words=num_features, split=' ')
tokenizer.fit_on_texts(data['review'].values)

# Transform text to sequences
X = tokenizer.texts_to_sequences(data['review'].values)
X = pad_sequences(X, maxlen=80)

# Transform labels to binary class matrices
Y = pd.get_dummies(data['sentiment']).values
print(Y)
# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Number of classes (2 - positive or negative)
num_classes = 2

# Maximum length of the reviews
max_len = 80

# Embedding dimensions
embed_dim = 128

# LSTM units
lstm_out = 196

# Dropout rate
dropout_rate = 0.2

# Create the model
model = Sequential()
model.add(Embedding(num_features, embed_dim, input_length=max_len))
model.add(SpatialDropout1D(dropout_rate))
model.add(LSTM(lstm_out, dropout=dropout_rate, recurrent_dropout=dropout_rate))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training the model
model.fit(X_train, Y_train, epochs=2, batch_size=16, verbose=1)

# Evaluating the model
accr = model.evaluate(X_test, Y_test)
print('Test set\n Loss: {:0.3f}\n Accuracy: {:0.3f}'.format(accr[0], accr[1]))
text_val = [
"This is a typical Steele novel production in that two people who have undergone some sort of tragedy manage to get together despite the odds. I wouldn't call this a spoiler because anyone who has read a Steele novel knows how they ALL end. If you don't want to know much about the plot, don't keep reading.<br /><br />Gilbert's character, Ophelia, is a woman of French decent who has lost her husband and son in an accident. Gilbert needs to stop doing films where she is required to have an accent because she, otherwise a good actress, cannot realistically pull off any kind of accent. Brad Johnson, also an excellent actor, is Matt, who is recovering from a rather nasty divorce. He is gentle, convincing and compelling in this role.<br /><br />The two meet on the beach through her daughter, Pip, and initially, Ophelia accuses Matt of being a child molester just because he talked art with the kid. All of them become friends after this episode and then the couple falls in love.<br /><br />The chemistry between the two leads is not great, even though the talent of these two people is not, in my opinion, a question. They did the best they could with a predictable plot and a script that borders on stereotypical. Two people meet, tragedy, bigger tragedy, a secret is revealed, another tragedy, and then they get together. I wish there was more to it than that, but there it is in a nutshell.<br /><br />I wanted mindless entertainment, and I got it with this. In regard to the genre of romantic films, this one fails to be memorable. ""A Secret Affair"" with Janine Turner is far superior (not a Steele book), as are some of Steele's earlier books turned into film."
,"This film took me by surprise. I make it a habit of finding out as little as possible about films before attending because trailers and reviews provide spoiler after spoiler. All I knew upon entering the theater is that it was a documentary about a long married couple and that IMDb readers gave it a 7.8, Rotten Tomatoes users ranked it at 7.9 and the critics averaged an amazing 8.2! If anything, they UNDERRATED this little gem.<br /><br />Filmmaker Doug Block decided to record his parents ""for posterity"" and at the beginning of the film we are treated to the requisite interviews with his parents, outspoken mother Mina, and less than forthcoming dad, Mike. I immediately found this couple interesting and had no idea where the filmmaker (Mike & Mina's son Doug) was going to take us. As a matter of fact, I doubt that Doug himself knew where he was going with this!<br /><br />Life takes unexpected twists and turns and this beautifully expressive film follows the journey. It is difficult to verbalize just how moved I was with this story and the unique way in which it was told. Absolutely riveting from beginning to end and it really is a must-see even if you aren't a fan of the documentary genre. This film will make you think of your own life and might even evoke memories that you thought were long forgotten. ""51 Birch Street"" is one of those rare filmgoing experiences that makes a deep impression and never leaves you. The best news of all is that HBO had a hand in the production so instead of playing to a limited art house audience, eventually, millions of people will have a chance to view this incredible piece of work. BRAVO!!!!!!!!"
,"Preston Sturgis' THE POWER AND THE GLORY was unseen by the public for nearly twenty or thirty years until the late 1990s when it resurfaced and even showed up on television. In the meantime it had gained in notoriety because Pauline Kael's THE CITIZEN KANE BOOK had suggested that the Herman Mankiewicz - Orson Welles screenplay for KANE was based on Sturgis' screenplay here. As is mentioned in the beginning of this thread for the film on the IMDb web site, Kael overstated her case.<br /><br />There are about six narrators who take turns dealing with the life of Charles Foster Kane: the newsreel (representing Ralston - the Henry Luce clone), Thatcher's memoirs, Bernstein, Jed Leland, Susan Alexander Kane, and Raymond the butler. Each has his or her different slant on Kane, reflecting their faith or disappointment or hatred of the man. And of course each also reveals his or her own failings when they are telling their version of Kane's story. This method also leads to frequent overlapping re-tellings of the same incident.<br /><br />This is not the situation in THE POWER AND THE GLORY. Yes, like KANE it is about a legendary business leader - here it is Tom Garner (Spencer Tracy), a man who rose from the bottom to being head of the most successful railroad system in the country. But there are only two narrators - they are Garner's right hand man Henry (Ralph Morgan) and his wife (Sarah Padden). This restricts the nearly three dimensional view we get at times of Kane in Garner. Henry, when he narrates, is talking about his boss and friend, whom he respected and loved. His wife is like the voice of the skeptical public - she sees only the flaws in Henry.<br /><br />Typical example: Although he worked his way up, Tom becomes more and more anti-labor in his later years. Unions are troublemakers, and he does not care to be slowed down by their shenanigans. Henry describes Tom's confrontation with the Union in a major walk-out, and how it preoccupied him to the detriment of his home life. But Henry's wife reminds him how Tom used scabs and violence to end the strike (apparently blowing up the Union's headquarters - killing many people). So we have two views of the man but one is pure white and one is pure black.<br /><br />I'm not really knocking THE POWER AND THE GLORY for not duplicating KANE's success (few films do - including all of Orson Welles' other films), but I am aware that the story is presented well enough to hold one's interest to the end. And thanks to the performances of Tracy and Colleen Moore as his wife Sally, the tragedy of the worldly success of the pair is fully brought home.<br /><br />When they marry, Tom wants to do well (in part) to give his wife and their family the benefits he never had. But in America great business success comes at a cost. Tom gets deeply involved with running the railroad empire (he expands it and improves it constantly). But it takes him away from home too much, and he loses touch with Sally. And he also notices Eve (Helen Vinson), the younger woman who becomes his mistress. When Sally learns of his unfaithful behavior it destroys her.<br /><br />Similarly Tom too gets a full shock (which makes him a martyr in the eyes of Henry). Eve marries Tom, and presents him with a son - but it turns out to be Eve's son by Tom's son Tom Jr. (Philip Trent). The discovery of this incestuous cuckolding causes Tom to shoot himself.<br /><br />The film is not a total success - the action jumps at times unconvincingly. Yet it does make the business seem real (note the scene when Tom tells his Board of Directors about his plans to purchase a small rival train line, and he discusses the use of debentures for financing the plans). Sturgis came from a wealthy background, so he could bring in this type of detail. So on the whole it is a first rate film. No CITIZEN KANE perhaps, but of interest to movie lovers as an attempt at business realism with social commentary in Depression America."
,"I first saw Thief as a child which makes me almost as old as the Jinn I guess. As any kid would be, I was delighted with the imagination, inventiveness and energy of the film. Several years later, I realized how much of the satire and wit of the script I had missed on that first viewing. I have never passed up an opportunity to watch it throughout the intervening years. In addition to the script, the production transcends the fantasy genre. This is Korda, the storyteller at his very best. When you see Thief as a child you know that you`ve had a great time. When you see Thief as an adult you know that you`ve seen a masterpiece. It`s as timeless as the story it treats. An amazing work.<br /><br />Thomas McCarthy"

]

'''
negative 
positive
positive
positive
'''

tokenizer.fit_on_texts(text_val)
 
# Transform text to sequences
complete = tokenizer.texts_to_sequences(text_val)
complete = pad_sequences(complete, maxlen=80)

predict = model.predict(complete)

# Convert probabilities to binary predictions (1 or 0) based on a threshold (e.g., 0.5)
threshold = 0.5
binary_predictions = (predict > threshold).astype(int)

print(binary_predictions)