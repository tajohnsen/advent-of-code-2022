fn main() {
    let in_file = include_str!("../../input")
        .split("\n\n")
        .collect::<Vec<&str>>()
        .into_iter()
        .map(|group| {
            //group.split("\n")
            //    .into_iter()
            group.lines()
                //.into_iter()
                .map(str::parse::<u32>)
                .map(Result::unwrap)
                .sum::<u32>()
        })
        .max()
        .unwrap();
        
        println!("{}\n", in_file);
/*
    in_file.for_each(|x| {
        println!("{}\n", x);
    })
    */
}

