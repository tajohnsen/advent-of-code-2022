/* I'm only doing part one because this language is awful. */

use std::collections::HashMap;

enum RPS {
    ROCK,
    PAPER,
    SCISSORS
}

enum WLD {
    WIN,
    LOSE,
    DRAW
}


impl RPS {
    fn value(&self) -> u32 {
        match *self {
            RPS::ROCK => 1,
            RPS::PAPER => 2,
            RPS::SCISSORS => 3,
        }
    }
}


impl WLD {
    fn value(&self) -> u32 {
        match *self {
            WLD::LOSE => 0,
            WLD::DRAW => 3,
            WLD::WIN => 6,
        }
    }
}


fn main() {
    let in_file = include_str!("../../input");

    let mut score1: HashMap<String, HashMap<String, u32>> = HashMap::new();
    let mut score1_rock: HashMap<String, u32> = HashMap::new();
    let mut score1_paper: HashMap<String, u32> = HashMap::new();
    let mut score1_scissors: HashMap<String, u32> = HashMap::new();

    score1_rock.insert(String::from("X"), RPS::ROCK.value() + WLD::DRAW.value()) ;
    score1_rock.insert(String::from("Y"), RPS::PAPER.value() + WLD::WIN.value()) ;
    score1_rock.insert(String::from("Z"), RPS::SCISSORS.value() + WLD::LOSE.value()) ;

    score1_paper.insert(String::from("X"), RPS::ROCK.value() + WLD::LOSE.value()) ;
    score1_paper.insert(String::from("Y"), RPS::PAPER.value() + WLD::DRAW.value()) ;
    score1_paper.insert(String::from("Z"), RPS::SCISSORS.value() + WLD::WIN.value()) ;

    score1_scissors.insert(String::from("X"), RPS::ROCK.value() + WLD::WIN.value()) ;
    score1_scissors.insert(String::from("Y"), RPS::PAPER.value() + WLD::LOSE.value()) ;
    score1_scissors.insert(String::from("Z"), RPS::SCISSORS.value() + WLD::DRAW.value()) ;

    score1.insert(String::from("A"), score1_rock);
    score1.insert(String::from("B"), score1_paper);
    score1.insert(String::from("C"), score1_scissors);

    let lines = in_file.lines();
    let mut total = 0;
    lines.for_each(|line| {
        let couple: Vec<&str> = line.split(' ').collect();
        total += score1.get(couple[0]).unwrap().get(couple[1]).unwrap();
    });
    println!("{}", total);
}
