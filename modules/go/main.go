package main

import "fmt"

type LabStatus struct {
    Mode string
    SimulationOnly bool
    NetworkAccess bool
}

func main() {
    status := LabStatus{"RED_HACKER", true, false}
    fmt.Printf("NATIONVK LAB: %+v\n", status)
}
