import SwiftUI
import Foundation

struct ContentView: View {
    @State var isOn = false
    @State var i = 0
    @State var red = 0.0
    var body: some View {
        VStack {
            Text("Magic Home")
                .font(.largeTitle)
                .fontWeight(.bold)
                .padding()
            VStack {
                Button(action: {
                    isOn = !isOn
                    print(shell("python3 -m flux_led 192.168.0.231 \(isOn ? "-1" : "-0")"))
                }, label: {
                    Image(systemName: "power")
                        .foregroundColor(isOn ? .green : .red)
                })
                HStack {
                    Button(action: {
                        print(shell("python3 -m flux_led 192.168.0.231 -c 255,133,51"))
                    }, label: {
                        Text(" ").font(.largeTitle)
                    })
                    .background(Color.init(red: 1, green: 133/255, blue: 51/255))
                    Button(action: {
                        print(shell("python3 -m flux_led 192.168.0.231 -c 0,255,170"))
                    }, label: {
                        Text(" ").font(.largeTitle)
                    })
                    .background(Color.init(red: 0, green: 1, blue: 170/255))
                    Button(action: {
                        print(shell("python3 -m flux_led 192.168.0.231 -c 255,0,0"))
                    }, label: {
                        Text(" ").font(.largeTitle)
                    })
                    .background(Color.init(red: 1, green: 0, blue: 0))
                }
//                Slider(value: $red, in: 0...255, step: 1.0, onEditingChanged: { (Bool) in
//
//                }, label: {
//
//                }).frame(width: 100, height: 100, alignment: .center)
            }
            .padding(.bottom)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

func shell(_ command: String) -> String {
    let task = Process()
    let pipe = Pipe()
    
    task.standardOutput = pipe
    task.standardError = pipe
    task.arguments = ["-c", command]
    task.launchPath = "/bin/zsh"
    task.launch()
    
    let data = pipe.fileHandleForReading.readDataToEndOfFile()
    let output = String(data: data, encoding: .utf8)!
    
    return output
}
