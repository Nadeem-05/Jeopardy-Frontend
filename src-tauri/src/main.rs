#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]


use tauri::api::process::Command;
use tauri::api::process::CommandEvent;

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}


fn main() {
    // `new_sidecar()` expects just the filename, NOT the whole path like in JavaScript
let (mut rx, mut child) = Command::new_sidecar("apps")
.expect("failed to create `apps` binary command")
.spawn()
.expect("Failed to spawn sidecar");

tauri::async_runtime::spawn(async move {
  // read events such as stdout
  while let Some(event) = rx.recv().await {
      if let CommandEvent::Stdout(line) = event {
          println!( "{}", line )
      }
  }
  });

    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
