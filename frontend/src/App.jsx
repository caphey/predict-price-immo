import React from "react";
import PredictionForm from "./components/PredictionForm";

const App = () => {
  return (
    <div className="min-h-screen bg-light">
      <h3 className="text-xl font-bold text-left py-8 pl-8">
        Prédiction de prix immobilier
      </h3>
      <div className="flex flex-col items-center justify-center ">
        <PredictionForm />
      </div>
    </div>
  );
};

export default App;
