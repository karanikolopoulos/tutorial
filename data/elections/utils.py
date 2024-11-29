choices = [
    "Democratic party",
    "Democratic candidate",
    "Democratic nominee",
    "Republican party",
    "Republican candidate",
    "Republican nominee",
]

def doc_to_choice(doc):
    return choices

def process_results(_, results):
    no_conts = int(len(choices) / 2)
    
    lls, _ = zip(*results)
    
    blue_acc = sum(lls[:no_conts])
    red_acc = sum(lls[no_conts:])
    
    return {"blue_acc": blue_acc, "red_acc": red_acc}