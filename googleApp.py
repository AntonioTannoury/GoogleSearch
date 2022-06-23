#%%
from search_engine_parser import GoogleSearch


def google(query):
    search_args = (query, 1)
    gsearch = GoogleSearch()
    gresults = gsearch.search(*search_args)
    return gresults["links"]


google("antonio")
# %%
