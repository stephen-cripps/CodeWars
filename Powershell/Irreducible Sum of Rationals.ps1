function get-gcd($a, $B) {
    while (1) {
        $rem = $a % $b
        if ($rem -eq 0) {
            return $b
        }
        $a = $b
        $b = $rem
    }
}

function sum-fracts($arr) {
    if ($arr.length -eq 0 ) {
        return "0"
    }
    
    $result = $arr[0]
    foreach ($item in @($arr | Select-Object -skip 1)) {
        $result[0] *= $item[1]
        $result[0] += $item[0] * $result[1]
        $result[1] *= $item[1]

        $gcd = get-gcd $result[0] $result[1]
        $result[0] /= $gcd
        $result[1] /= $gcd
    }

    if ( $result[1] -eq 1) {
        return $result[0]
    }
    
    return "[" + $result[0] + ", " + $result[1] + "]"
}

function testing($arr, $expect) {
    $ans = sum-fracts $arr
    $ans | Should Be $expect
}

function fixed() {
    $a = (1, 2), (1, 3), (1, 4)
    testing $a "[13, 12]"
    $a = (1, 2), (2, 9), (3, 18), (4, 24), (6, 48)
    testing $a "[85, 72]"  
    $a = @()
    testing $a "0"
    $a = @((7700000, 13000000), (8400000, 13100000), (6000000, 8000000))
    testing $a "[67559, 34060]"

}

Describe "sum-fracts" {
    Context "Fixed Tests" {
        It "Should Pass Fixed Tests" {
            fixed
        } 
    }
}
