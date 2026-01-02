"""
ExplainThis.ai - Comprehensive Testing Script
Run this to test your AI module before pushing to GitHub
Author: AI & QA Lead (Member 3)
"""

import os
import sys
from ai_service import ExplainThisAI
from prompts import PromptValidator

def print_section(title):
    """Pretty print section headers"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")

def test_single_mode(ai, query, mode):
    """Test a single mode and display results"""
    mode_names = {"1": "5-YEAR-OLD", "2": "TEENAGER", "3": "ADULT"}
    
    print(f"🔍 Testing Mode: {mode_names.get(mode, mode)}")
    print(f"📝 Query: {query}\n")
    
    result = ai.explain(query, mode=mode, validate=True)
    
    if result["success"]:
        print("✅ Status: SUCCESS")
        print(f"📊 Word Count: {result['word_count']}")
        print(f"✓ Validation: {'PASSED ✅' if result['validation_passed'] else 'FAILED ⚠️'}")
        
        if result.get("issues"):
            print(f"⚠️ Issues Found:")
            for issue in result['issues']:
                print(f"   - {issue}")
        
        if result.get("warning"):
            print(f"⚠️ Warning: {result['warning']}")
        
        print(f"\n{'─'*80}")
        print("📄 GENERATED EXPLANATION:")
        print(f"{'─'*80}\n")
        print(result["simplified"])
        print(f"\n{'─'*80}\n")
        
    else:
        print(f"❌ ERROR: {result.get('error')}")
    
    return result

def test_all_modes(ai, query):
    """Test all three modes for comparison"""
    print_section(f"TESTING ALL MODES - Query: '{query}'")
    
    results = ai.batch_explain(query)
    
    mode_names = {"1": "5-Year-Old", "2": "Teenager", "3": "Adult"}
    
    print(f"{'Mode':<15} | {'Status':<10} | {'Words':<8} | {'Validation':<12} | {'Issues'}")
    print(f"{'-'*80}")
    
    for mode, result in results.items():
        if result["success"]:
            status = "✅ SUCCESS"
            words = f"{result['word_count']:3} words"
            validation = "PASSED ✅" if result.get('validation_passed', False) else "FAILED ⚠️"
            issues = len(result.get('issues', []))
            
            print(f"{mode_names[mode]:<15} | {status:<10} | {words:<8} | {validation:<12} | {issues} issue(s)")
        else:
            print(f"{mode_names[mode]:<15} | ❌ FAIL    | N/A      | N/A          | Error: {result.get('error', 'Unknown')[:30]}")
    
    print()
    return results

def comprehensive_test():
    """Run comprehensive test suite"""
    
    # Check for API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ ERROR: GROQ_API_KEY not found in environment variables!")
        print("Set it using: export GROQ_API_KEY='your-key-here'")
        print("Or create a .env file with: GROQ_API_KEY=your-key-here")
        return False
    
    # Initialize AI
    print("🚀 Initializing ExplainThis.ai (Production Version)...")
    try:
        ai = ExplainThisAI(api_key)
        print("✅ AI Service initialized successfully!\n")
    except Exception as e:
        print(f"❌ Failed to initialize AI service: {e}")
        return False
    
    # Test queries (hackathon demo scenarios)
    test_queries = [
        "Machine Learning",
        "Blockchain Technology",
        "Quantum Computing",
        "Neural Networks"
    ]
    
    all_results = []
    
    # Test 1: Quick validation test
    print_section("TEST 1: QUICK VALIDATION (Teenager Mode)")
    result = test_single_mode(ai, test_queries[0], "2")
    all_results.append(result)
    
    # Test 2: All modes comparison
    print_section("TEST 2: ALL MODES COMPARISON")
    results = test_all_modes(ai, test_queries[1])
    all_results.extend(results.values())
    
    # Test 3: Detailed 5-year-old mode test (most critical)
    print_section("TEST 3: DETAILED 5-YEAR-OLD MODE TEST")
    kid_result = test_single_mode(ai, test_queries[2], "1")
    all_results.append(kid_result)
    
    # Test 4: Adult mode business focus test
    print_section("TEST 4: ADULT MODE BUSINESS FOCUS TEST")
    adult_result = test_single_mode(ai, test_queries[3], "3")
    all_results.append(adult_result)
    
    # Summary
    print_section("TEST SUMMARY")
    
    successful = sum(1 for r in all_results if r.get("success", False))
    validated = sum(1 for r in all_results if r.get("validation_passed", False))
    total = len(all_results)
    
    print(f"📊 Results:")
    print(f"   ✅ Successful: {successful}/{total}")
    print(f"   ✓ Validated: {validated}/{total}")
    print(f"   ❌ Failed: {total - successful}/{total}")
    
    print(f"\n{'─'*80}")
    print("🎯 Next Steps:")
    
    if successful == total and validated >= total * 0.7:  # 70% validation pass rate
        print("   ✅ All tests passed! Ready to push to GitHub.")
        print("   📋 Run: git add . && git commit -m 'AI module complete' && git push")
        success_status = True
    elif successful == total:
        print("   ⚠️ All tests successful but some validation issues.")
        print("   💡 Review validation issues and consider adjusting prompts.")
        print("   ✅ Still acceptable for push if responses look good.")
        success_status = True
    else:
        print("   ⚠️ Some tests failed. Review errors and retry.")
        print("   💡 Check API key, network connection, and error messages.")
        success_status = False
    
    print(f"{'─'*80}\n")
    
    return success_status

def quick_test():
    """Quick test for rapid iteration"""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ Set GROQ_API_KEY first!")
        print("Create a .env file with: GROQ_API_KEY=your-key-here")
        return
    
    ai = ExplainThisAI(api_key)
    
    # Quick test with Machine Learning
    query = input("Enter topic to explain (or press Enter for 'Machine Learning'): ").strip()
    if not query:
        query = "Machine Learning"
    
    mode = input("Mode (1/2/3 for 5-year-old/teenager/adult, default: 2): ").strip()
    if not mode or mode not in ["1", "2", "3"]:
        mode = "2"
    
    result = test_single_mode(ai, query, mode)
    
    print("\n💾 Save this output? (y/n): ", end="")
    if input().lower() == 'y':
        filename = f"test_output_mode{mode}_{query.replace(' ', '_')}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Query: {query}\n")
                f.write(f"Mode: {mode}\n")
                f.write(f"Word Count: {result.get('word_count', 'N/A')}\n")
                f.write(f"Validation: {'PASSED' if result.get('validation_passed') else 'FAILED'}\n")
                f.write(f"\n{'='*80}\n\n")
                f.write(result.get('simplified', 'No output'))
            print(f"✅ Saved to {filename}")
        except Exception as e:
            print(f"❌ Failed to save: {e}")

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        quick_test()
    else:
        success = comprehensive_test()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
