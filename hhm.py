import datashape
import texttable as tt
table = tt.texttable()
table.add_rows[(None,None,None,None,)] + datashape
table.set_cols_align(('c','c','c','c'))
table.header(('Counrty','Number of case','Deaths', 'Continet'))
print(table.draw())