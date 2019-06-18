fn maxFraction(numerators: Vec<i32>, denominators: Vec<i32>) -> i32 {
    let mut r = 0;
    for i in 1..numerators.len() {
        if numerators[i] * denominators[r] > numerators[r] * denominators[i] {
            r = i;
        }
    }
    r as i32
}
