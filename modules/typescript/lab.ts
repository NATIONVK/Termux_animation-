export type LabMode = "RED_HACKER" | "BLUE_HEART" | "MATRIX";
export interface LabStatus {
  mode: LabMode;
  simulationOnly: true;
  networkAccess: false;
}
export function getLabStatus(mode: LabMode = "RED_HACKER"): LabStatus {
  return { mode, simulationOnly: true, networkAccess: false };
}
