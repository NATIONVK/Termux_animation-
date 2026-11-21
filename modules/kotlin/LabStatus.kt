package com.nationvk.lab

data class LabStatus(
    val mode: String = "RED_HACKER",
    val simulationOnly: Boolean = true,
    val networkAccess: Boolean = false
)
