import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Label } from "@/components/ui/label"

const PsychTest = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [showResults, setShowResults] = useState(false);
  const [results, setResults] = useState({});
  const router = useRouter();

  // Sample questions (replace with your actual questions)
  const questions = [
    {
      question: "I enjoy being the center of attention.",
      options: ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    },
    {
      question: "I often feel anxious in social situations.",
      options: ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    },
    // Add more questions here
  ];

  const handleAnswer = (answer) => {
    setAnswers({...answers, [currentQuestion]: answer});
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    }
  };

  const calculateResults = () => {
    // This is a placeholder. Replace with your actual calculation logic
    const score = Object.values(answers).reduce((sum, value) => sum + value, 0);
    setResults({ score: score, description: "This is your result description." });
    setShowResults(true);
  };

  const resetTest = () => {
    setCurrentQuestion(0);
    setAnswers({});
    setShowResults(false);
    setResults({});
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <Card className="w-full max-w-md mx-auto">
        <CardHeader>
          <CardTitle>Psychological Test</CardTitle>
          <CardDescription>Answer the following questions honestly.</CardDescription>
        </CardHeader>
        <CardContent>
          {!showResults ? (
            <>
              <h2 className="text-xl font-bold mb-4">{questions[currentQuestion].question}</h2>
              <RadioGroup onValueChange={handleAnswer} value={answers[currentQuestion]}>
                {questions[currentQuestion].options.map((option, index) => (
                  <div key={index} className="flex items-center space-x-2">
                    <RadioGroupItem value={index} id={`option-${index}`} />
                    <Label htmlFor={`option-${index}`}>{option}</Label>
                  </div>
                ))}
              </RadioGroup>
            </>
          ) : (
            <div>
              <h2 className="text-xl font-bold mb-4">Your Results</h2>
              <p>Score: {results.score}</p>
              <p>{results.description}</p>
            </div>
          )}
        </CardContent>
        <CardFooter className="flex justify-between">
          {!showResults ? (
            <>
              {currentQuestion > 0 && (
                <Button onClick={() => setCurrentQuestion(currentQuestion - 1)}>Previous</Button>
              )}
              {currentQuestion < questions.length - 1 ? (
                <Button onClick={() => setCurrentQuestion(currentQuestion + 1)}>Next</Button>
              ) : (
                <Button onClick={calculateResults}>Submit</Button>
              )}
            </>
          ) : (
            <>
              <Button onClick={resetTest}>Retake Test</Button>
              <Button onClick={() => router.push('/')}>Home</Button>
            </>
          )}
        </CardFooter>
      </Card>
    </div>
  );
};

export default PsychTest;
