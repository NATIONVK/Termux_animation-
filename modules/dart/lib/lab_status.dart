class LabStatus {
  final String mode;
  final bool simulationOnly;
  final bool networkAccess;

  const LabStatus({
    this.mode = 'RED_HACKER',
    this.simulationOnly = true,
    this.networkAccess = false,
  });
}
