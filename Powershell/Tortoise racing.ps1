function race($v1, $v2, $g) {
    if ($v1 -gt $v2 -or $v1 -eq $v2) {
        return "-1 -1 -1"
    }

    $timer = $g / ($v2 - $v1); 

    $Hours = [Math]::Floor($timer)
    $timer = ($timer - $hours) * 60
    $minutes = [Math]::Floor([Math]::Round($timer, 3))
    $timer = ($timer - $minutes) * 60
    $seconds = [Math]::Abs([Math]::Floor([Math]::Round($timer, 3)))

    return "" + ($hours, $minutes, $seconds )
}


function testing($v1, $v2, $g, $expect) {
    $ans = race $v1 $v2 $g
    $ans | Should Be $expect
}

function fixed() {
    testing 720 850 70 "0 32 18"
    testing 820 850 550 "18 20 0"
    testing 820 81 550 "-1 -1 -1"
    
}

Describe "race" {
    Context "Fixed Tests" {
        It "Should Pass Fixed Tests" {
            fixed
        } 
    }
}