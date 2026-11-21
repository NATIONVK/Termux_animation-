-- Lightweight status module for local simulation.
local Lab = {}
function Lab.status()
  return {
    project = "NATIONVK RED HACKER LAB",
    mode = "SIMULATION",
    network_access = false
  }
end
return Lab
