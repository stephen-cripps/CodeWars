fn main() {
    println!("{}", solution("Hello, world!"));
}

fn solution(phrase: &str) -> String {
    let mut bytes = phrase.as_bytes().to_vec();

    bytes.reverse();

    String::from_utf8(bytes).unwrap()
}
