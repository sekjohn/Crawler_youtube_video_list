//
//  testApp.swift
//  test WatchKit Extension
//
//  Created by lionrocket on 2021/03/09.
//

import SwiftUI

@main
struct testApp: App {
    @SceneBuilder var body: some Scene {
        WindowGroup {
            NavigationView {
                ContentView()
            }
        }

        WKNotificationScene(controller: NotificationController.self, category: "myCategory")
    }
}
