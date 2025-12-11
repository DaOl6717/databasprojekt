import saxonche

proc = saxonche.PySaxonProcessor(license=False)
xquery_processor = proc.new_xquery_processor()

file = proc.parse_xml(xml_file_name="ProductsBySupplier.xml") # Replace with your file
xquery_processor.set_context(xdm_item = file)

def run_query(query: str):
	xquery_processor.set_query_content(query) # Replace with your query
	result = xquery_processor.run_query_to_string()
	print(result)
	xquery_processor.clear_properties()

query1 = """for $i in goods/entry where $i/quantity > 5 and $i/discount > 10
				order by xs:integer($i/discount) descending
				return $i"""

# run_query(query1)

query2 = """for $i in goods/entry where $i/category = 'Tablet'
				order by xs:integer($i/price) ascending
				return $i"""

# run_query(query2)

query3 = """let $sorted := for $e in goods/entry order by xs:integer($e/discount) descending return $e
		   let $max_discount := $sorted[1]/discount
		   for $e in goods/entry where $e[discount = $max_discount] return $e"""

# run_query(query3)

query4 = """goods/entry[name='Winovo Thinkpod P16']/price"""

# run_query(query4)

# Elbin/Lbin

query5 = """for $category in ('Desktop', 'Laptop', 'Tablet')
				let $sorted := for $i in goods/entry where $i/category = $category order by xs:integer($i/price) ascending return $i
				let $cheapest_price := $sorted[1]/price
				return goods/entry[category = $category and price = $cheapest_price]"""

run_query(query5)