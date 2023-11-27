import pyterrier as pt
import pandas as pd


# DEFINING HELPER FUNCTIONS

def get_exp_title(docid):
  id = int(docid[1:])
  return exp_title[id]

def get_exp_link(docid):
  id = int(docid[1:])
  return exp_link[id]

def get_exp_description(docid):
  id = int(docid[1:])
  return exp_desc[id]

def get_exp_subject(docid):
  id = int(docid[1:])
  return exp_subj[id]

def get_exp_explanation(docid):
  id = int(docid[1:])
  return exp_expl[id]

def retrieve_exp(df):
  title = []
  link = []
  desc = []
  subject = []
  explanation = []
  for i in range(df.shape[0]):
    docid = df.loc[i, 'docno']
    title.append(get_exp_title(docid))
    link.append(get_exp_link(docid))
    desc.append(get_exp_description(docid))
    subject.append(get_exp_subject(docid))
    explanation.append(get_exp_explanation(docid))
  df['title'] = title
  df['link'] = link
  df['description'] = desc
  df['subject'] = subject
  df['explanation'] = explanation
  return df



# Start pyterrier
if not pt.started():
  pt.init()


# Get and merge all json files
docs_df = pd.read_json("./science_experiments/experiment_archive.json")

docs_df_2 = pd.read_json("./science_experiments/steve_spangler.json")
docs_df_2 = docs_df_2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

docs_df_3 = pd.read_json("./science_experiments/science_buddies.json")
docs_df_3 = docs_df_3.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


docs_df = pd.concat([docs_df, docs_df_2], ignore_index=True)
docs_df = pd.concat([docs_df, docs_df_3], ignore_index=True)
docs_df = docs_df.fillna('')
docs_df = docs_df.loc[docs_df["explanation"] != ""]


docno = ['d'+ str(i) for i in range(docs_df.shape[0])]
docs_df['docno'] = docno
docs_df['text'] = docs_df['title'] + ' ' + docs_df['subject'] + ' ' + docs_df['explanation']

exp_title = docs_df.title.values
exp_link = docs_df.link.values
exp_desc = docs_df.description.values
exp_subj = docs_df.subject.values
exp_expl = docs_df.explanation.values

# index every science experiment
indexer = pt.DFIndexer("./index_3docs", overwrite=True)
index_ref = indexer.index(docs_df['text'], docs_df['docno'])
index = pt.IndexFactory.of(index_ref)

# define retrieval function
br = pt.BatchRetrieve(index, wmodel="BM25")

