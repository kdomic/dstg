<?php
	
	//$arr = array(array($_GET['lat'],$_GET['lng']));
	//echo json_encode($arr, JSON_FORCE_OBJECT);
	
	exec("python dijkstra.py ".$_GET['lat']." ".$_GET['lng'], $output); //echo implode( "\n", $output );
	$raw = explode(";", implode( "\n", $output ));	
	$arr = array();
	foreach($raw as $marker ){
		$coords = explode(",", $marker);
		array_push($arr, array($coords[0],$coords[1]) );
	}
	echo json_encode($arr, JSON_FORCE_OBJECT);
?>
