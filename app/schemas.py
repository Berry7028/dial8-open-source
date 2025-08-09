from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any


@dataclass
class Segment:
    startMs: int
    endMs: int
    text: str
    speakerId: Optional[str] = None
    confidence: Optional[float] = None


@dataclass
class TranscriptResult:
    id: str
    language: str
    segments: List[Segment] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "language": self.language,
            "segments": [asdict(s) for s in self.segments],
        }


class CreateTranscriptionResponse:
    id: str
    status: str


class GetTranscriptionStatusResponse:
    id: str
    status: str
    progress: Optional[float] = None


class ErrorResponse:
    error: dict