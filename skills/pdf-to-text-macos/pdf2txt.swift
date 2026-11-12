import PDFKit
import Foundation
let a = CommandLine.arguments
if let d = PDFDocument(url: URL(fileURLWithPath: a[1])) {
  try? (d.string ?? "").write(toFile: a[2], atomically: true, encoding: .utf8)
  print(a[1], d.pageCount)
}
