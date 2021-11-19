import chardet

class InteractiveDetector(chardet.UniversalDetector):
    def close(self):
        super().close()
        if self.result['encoding'] == "ascii":
            return self.result
        else:
            self.result = []
            for prober in self._charset_probers:
                if not prober:
                    continue
                confidence = prober.get_confidence()
                charset = prober.charset_name
                if charset:
                    if charset.lower().startswith("iso-8859"):
                        if self._has_win_bytes:
                            charset = self.ISO_WIN_MAP.get(charset.lower(), charset)
                    self.result.append({
                        "encoding": charset,
                        "confidence": confidence,
                        "language": prober.language
                    })
            self.result.sort(key=lambda item: -item['confidence'])
            return self.result


