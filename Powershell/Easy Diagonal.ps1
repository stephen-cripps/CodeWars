$pyramid = @{"0 0" = 1 }
function getValue($row, $col) {
    $key = "" + $row + " " + $col

    if ($null -eq $pyramid[$key]) {
        if ($col -eq 0 -or $row -eq $col) {
            $pyramid[$key] = 1
        }
        else {
            $ul = getValue ($row - 1) ($col - 1)
            $ur = getValue ($row - 1) $col
            $pyramid[$key] = $ul + $ur
        }
    }
    return $pyramid[$key]
}

function diagonal($n, $p) {
    $sum = 0
    for ($i = $p; $i -lt ($n + 1); $i++) {
        $sum += getValue $i $p
    }
    return $sum
}

function testing($n, $p, $expect) {
    $ans = diagonal $n $p
    $ans | Should Be $expect
}

function fixed() {
    testing 7 0  8
    testing 20 3  5985
    testing 20 4  20349
    testing 20 5  54264
    testing 20 15  20349
    
}

Describe "diagonal" {
    Context "Fixed Tests" {
        It "Should Pass Fixed Tests" {
            fixed
        } 
    }
}