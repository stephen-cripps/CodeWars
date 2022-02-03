function nb-dig($n, $d)
{
   $target = [string]$d
$count = 0
    for ($i= 0; $i <= $n; $i++  ){
      $square = ([string]($i*$i)).toCharArray()
      
     foreach ($char in $array){
         if($char == $target){
         count++
         }
     }
    }
    return count; 
}