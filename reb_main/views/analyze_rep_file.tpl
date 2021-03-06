<!doctype html>

<html>
	<head>
		<title>Rebataur Config</title>
		<script>
		</script>
		
		<style>
			div.rep_files{
				padding:0.4em;
			}
			div.rep_files > a{
				padding-left:100px;
			}
		</style>
		

		<script type="text/javascript" src="/static/js/jquery.js"></script>
		<script>
			var fct_idx = 0;
			var msr_idx = 0;
			$(document).ready(function(){
				
				$("a#add_primary_keys").on("click",function(){
					get_tables("primary",fct_idx++);
				});	
				$("a#add_measures").on("click",function(){
					get_tables("measures",msr_idx++);
				});	
				
			});


			function get_tables(cmd,idx){

				get_data("get","tables","",function(result){
					var options = "<option></option>";
		
					for( var i =0; i<result.length; i++){
						options += "<option class='tbl' value='"+ result[i]+"'>" + result[i]+ 
								"</option>";				
					}

					var table = "<td>" +
							"<select name='"+ idx +"'>"+ options +"</select>" +
			 			    "</td><td align='center'>=</td>";
					if(cmd == "primary"){
						$("tr#primary_keys").append(table);
					}else if( cmd == "measures"){
						table = "<tr>" + table + "</tr>";
						$("tbody#measures").append(table);
					}else{
						$("tr#primary_keys").html(table);
					}
					
					$("option.tbl").on('click',function(evt){
						add_cols($(this),idx,cmd);
					});
					

				});


				
			}
			function add_cols(evt,idx,cmd){
				idx += 100;
				var cols = get_data( "get","cols",evt.attr("value"),function(result){
					var options = "<option></option>";
		
					for( var i =0; i<result.length; i++){
						options += "<option class='col' value='"+ result[i]+"'>" + result[i]+ 
								"</option>";				
					}

					var select = "<select name='"+  idx +"'>"+ options +"</select>" ;		
						
					evt.parent().parent().find("select > option.col").parent().remove();	 			   
					evt.parent().after(select);

					if( cmd == "measures"){
						var select = "<select name='dt_type_"+  idx +"'>"+ get_dt_options() +"</select>" ;
								
						evt.parent().after(select);
					}
					else if( cmd == "primary"){
						var select = "<select name='primary_key_"+  idx +"'>"+ options +"</select>" ;		
						
						//evt.parent().parent().find("select > option.col").parent().remove();	 			   
						evt.parent().after(select);
					}
		


					
						
				});
				

				
			}
			function get_dt_options(){
				var dt_option = "" ; 
				var dt_types = ["int","numeric","string","loc","date","time","datetime"];
				for (var i =0; i< dt_types.length; i++){
					dt_option += "<option class='col' value='" + dt_types[i] + "'>"+dt_types[i]+"</option>";
				}
				return dt_option;

				
			}	
					
			
			function get_data(cmd,key,val,callback){
				$.ajax({
					method:"POST",
					url : "/query",
					data : {"cmd":cmd, "key":key, "val":val}		
				}).done(function(result){
					callback(JSON.parse(result));				
				});
			}

		</script>
	</head>


	<body>

<div>
	<a href="config">Configuration</a>
	<a href="wizard">Wizard</a>
	<a href="analytics">Analytics</a>
</div>


<h4>Add keys</h4>
<form method="POST" action="fact/save_keys">
<labe>Fact Table Name</label><input type="text" name="fact_table_name"/>
<table>
<thead>
	<th><td>Select Table, Primary key and fact key</td></th>
</thead>
<tbody>
	<tr id="primary_keys">		
	</tr>
	<tr>
		<td><a href=# id="add_primary_keys">Add</a></td>
	</tr>

	<tr><td><button type="submit">Save</button>
</tbody>

</table>
</form>



<h4>Add Measures</h4>

<form method="POST" action="fact/save_measures">

<labe>Fact Table Name</label><input type="text" name="fact_table_name"/>
<table>
<tbody id="measures">
	

	<tr>
		<td><a href=# id="add_measures">Add</a></td>
	</tr>

	<tr><td><button type="submit">Save</button>
</tbody>

</table>
</form>


</body>


</html>


