#[derive(Debug)]
struct LabStatus {
    mode: &'static str,
    simulation_only: bool,
    network_access: bool,
}

fn main() {
    let status = LabStatus {
        mode: "RED_HACKER",
        simulation_only: true,
        network_access: false,
    };
    println!("NATIONVK LAB: {status:?}");
}
