import re

def apply_cleaner(text):
    # First we lower case the text
    text = text.lower()
    # remove links
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', text)
    # Remove usernames
    text = re.sub('@[^\s]+', '', text)
    # replace hashtags by just words
    text = re.sub(r'#([^\s]+)', r'\1', text)
    # correct all multiple white spaces to a single white space
    text = re.sub('[\s]+', ' ', text)
    # Additional clean up : removing words less than 3 chars, and remove space at the beginning and teh end
    text = re.sub(r'\W*\b\w{1,2}\b', '', text)
    return text

def reformat_pred(pred, texts):
    labels = pred[0]
    labels = [label[0] for label in labels]
    scores = pred[1]
    scores = [sc.item() for sc in scores]
    pred_out = zip(labels, scores, texts)
    return pred_out
    #print([*pred_out])