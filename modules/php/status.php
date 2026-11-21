<?php
// Local-only status endpoint example; no server is started by this file.
header('Content-Type: application/json; charset=utf-8');
echo json_encode([
    'project' => 'NATIONVK RED HACKER LAB',
    'mode' => 'SIMULATION',
    'network_access' => false
], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
