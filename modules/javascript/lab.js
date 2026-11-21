// NATIONVK browser-side simulation utilities.
export const labStatus = () => ({
  name: "NATIONVK RED HACKER LAB",
  mode: "SIMULATION",
  networkAccess: false
});

export function makeLog(message, level = "INFO") {
  const safe = String(message).replace(/[<>]/g, "");
  return { time: new Date().toISOString(), level, message: safe };
}
